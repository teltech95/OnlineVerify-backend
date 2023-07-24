
const myForm = document.getElementById("email-list");

function addEmailField() {
// Create elements
const nef_wrapper = document.createElement("div");
const nef = document.createElement("input");
const btnAdd = document.createElement("button");
const btnDel = document.createElement("button");

// Add Class to main wrapper
nef_wrapper.classList.add("email-input__w");

// set button ADD
btnAdd.type = "button";
btnAdd.classList.add("btn-add-input");
btnAdd.innerText = "+";
btnAdd.setAttribute("onclick", "addEmailField()");

// set button DEL
btnDel.type = "button";
btnDel.classList.add("btn-del-input");
btnDel.innerText = "-";

// set Input field
nef.type = "email";
nef.name = "email_field";
nef.setAttribute("required", "");
nef.classList.add("input-field");

//append elements to main wrapper
nef_wrapper.appendChild(nef);
nef_wrapper.appendChild(btnAdd);
nef_wrapper.appendChild(btnDel);

// append element to DOM
myForm.appendChild(nef_wrapper);
btnDel.addEventListener("click", removeEmailField);
}

//remove element from DOM
function removeEmailField(el) {
const field = el.target.parentElement;
field.remove();
}

