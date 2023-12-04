/* Function that extracts credentials from the form
 * and sends them to backend for validation */
async function handleRegisterForm(form){
  const email_address = form.email_address.value;
  const password = form.password.value;

  let msu_email_regex = new RegExp('[a-z0-9]+@montclair.edu$');

  if (!msu_email_regex.test(email_address)){
    console.log("Invalid MSU email address !");
    return
  }

  if (!email_address || !password){
    console.log("Please fill all the fields !");
	  return
  }

  const credentials = new FormData(form);

  const config = {
    method: "POST",
    mode: "cors",
    headers: {
        "Access-Control-Allow-Origin": "http://127.0.0.1:21854/",
    },
    body: credentials
  }

  const response = await fetch("http://127.0.0.1:5000/api/v1/register", config);
  const data = await response.json();
  console.log(data);
}
