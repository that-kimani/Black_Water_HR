// Toggle password visibility
document.getElementById('toggle-password').addEventListener('click', function() {
    var passwordField = document.getElementById('password');
    var passwordFieldType = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = passwordFieldType;
    this.classList.toggle('fa-eye');
    this.classList.toggle('fa-eye-slash');
});

// Function responsible for decoding the JWT token.
function parseJWT(token) {

    try {

        const base64Url = token.split('.')[1];
        const base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');

        const jsonPayload = decodeURIComponent(

        atob(base64)
                .split('')
                .map(c => '%' + ('00' + c.charCodeAt(0).toString(16)).slice(-2))
                .join('')

        );

        return JSON.parse(jsonPayload);
        } 

        catch (error) {
            return null;   
        }
        }


// Handle the login action.
document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const employeeId = document.getElementById('employee-id').value;
    const password = document.getElementById('password').value;

    try {

        // Make an authentication request to see if the user credentials are authentic.
        const authentication_response = await fetch('api/auth/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },

            body: JSON.stringify({
                employee_id: employeeId,
                password: password
            })

        });


        // if the user exists, we are served an acces and refresh token.
        // We'll store those tokens in the local storage.
        const authData = (await authentication_response.json());

        const JWT_access_token = authData['access'];
        const JWT_refresh_token = authData['refresh'];

        localStorage.setItem('refresh_token' , JWT_refresh_token);
        localStorage.setItem('access_token' , JWT_access_token);

        // We'll retrieve the access token and decode it so that we can know what the
        // user's role is. This way, we can redirect them to the needed url.
        const token = localStorage.getItem('access_token');

        // Redirect the user based on their employee category.
        const payload = parseJWT(token)
        if (payload) {
            // Log the employee category of the user.
            console.log(payload.staff_category)

            // Redirect accordingly
            if (payload.staff_category === 'HR') {
                window.location.href = 'api/hr/hr-dashboard'
            }
            else {
                window.location.href = 'api/staff/staff-dashboard'
            }
        }

    } catch (error) {
        document.getElementById('error-message').textContent = error ;// 'An error occurred. Please try again later.';
    }
});