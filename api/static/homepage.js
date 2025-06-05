// Toggle password visibility
document.getElementById('toggle-password').addEventListener('click', function() {
    var passwordField = document.getElementById('password');
    var passwordFieldType = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = passwordFieldType;
    this.classList.toggle('fa-eye');
    this.classList.toggle('fa-eye-slash');
});



document.getElementById('login-form').addEventListener('submit', async function (e) {
    e.preventDefault();

    const employeeId = document.getElementById('employee-id').value;
    const password = document.getElementById('password').value;

    try {

        // make an authentication request to see if the user credentials are authentic.
        const authentication_response = await fetch('api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },

            body: JSON.stringify({
                employee_id: employeeId,
                password: password
            })

        });


        // if the user exists and we were served a token and their employe category.
        // We'll store that data in the local storage.
        const JWT_token = (await authentication_response.json())['token'];

        localStorage.setItem('token' , JWT_token);


        // Now send the redirection authorization request to the api, along with our token.
        // The api will give us the url we are authorized to access, based on our registered employee category.
        const authorization_response = await fetch('api/redirect', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization' : ('Bearer ' + localStorage.getItem('token')),
            },

        });


        // Now redirect the user to the url that was provided by the api.
        if (authorization_response.ok) {

            const data = await authorization_response.json();
            window.location.href = data.redirect_url;

        } 
        else if (authorization_response.status == 403) {
            window.location.href = 'unauthorized';

        }

        else {
            alert('Something wnt wrong.');
        }


    } catch (error) {
        document.getElementById('error-message').textContent = error ;// 'An error occurred. Please try again later.';
    }
});