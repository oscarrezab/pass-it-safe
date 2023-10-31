// display modal on click

const modalWrapper = document.querySelector(".modals-wrapper");
if (modalWrapper){
    function displayModal(id){
        const modal = document.getElementById(id);
        modalWrapper.style.display = "flex";
        modal.style.display = "flex";
        // close modal
        const close = document.getElementById("close-modal");
        close.addEventListener("click", () =>{
            modalWrapper.style.display = "none";
            modal.style.display = "none"; 
            document.querySelector("header").style.display = "unset";
            document.querySelector("footer").style.display = "unset";    
        })
        document.querySelector("header").style.display = "none";
        document.querySelector("footer").style.display = "none";
    }
}


// copy elements
function copyEmail() {
    var inputElement = document.getElementById("email");
    var textToCopy = inputElement.value;
    navigator.clipboard.writeText(textToCopy);
};

function copyPass() {
    var inputElement = document.getElementById("password");
    var textToCopy = inputElement.value;
    navigator.clipboard.writeText(textToCopy);
};


// Dsplay actions of password card for mobile devices
const actions = document.querySelectorAll(".actions");
if (actions){
    actions.forEach(action =>{
        action.onclick = () =>{
            const links = action.querySelectorAll("a");
            links.forEach(link =>{
                link.style.display = "flex";
            })
            setTimeout(function(){
                links.forEach(link =>{
                    link.style.display = "none";
                })}, 3000)
        }
    })
}