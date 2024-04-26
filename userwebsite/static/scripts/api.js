var token = localStorage.getItem('token');
function addTokenToHeaders(token) {
    if (token) {
        // Add token to request headers
        fetchOptions.headers = {
            'Authorization': 'Bearer ' + token
        };
    }
}

var fetchOptions = {
    headers: {
        'Content-Type': 'application/json'
    }
};

addTokenToHeaders(token);
