/* Function that extracts credentials from the form
 * and sends them to backend for validation */
async function handleLoginForm(form){
    const email_address = form.email_address.value;
    const password = form.password.value;
    const credentials = new FormData(form);

    const config = {
	method: "POST",
	headers: {
	    "Access-Control-Allow-Origin": "http://localhost:23733/",
	},
	body: credentials
    }
    const response = await fetch("http://127.0.0.1:5000/api/v1/login", config);
    const data = await response.json();
    console.log(data);
}
