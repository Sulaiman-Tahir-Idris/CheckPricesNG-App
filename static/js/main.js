const menuBtn = document.querySelector('.menu-btn');
const hamburger = document.querySelector('.menu-btn__burger');
const nav = document.querySelector('.nav');
const menuNav = document.querySelector('.menu-nav');
const navItems = document.querySelectorAll('.menu-nav__item');
let showMenu = false;
let select = document.getElementById("select");
let list = document.getElementById("list");
let selectText = document.getElementById("selectText");
let inputField = document.getElementById("inputfield");

let options = document.getElementsByClassName("options");

menuBtn.addEventListener('click', toggleMenu);

function toggleMenu() {
    if(!showMenu) {
        hamburger.classList.add('open');
        nav.classList.add('open');
        menuNav.classList.add('open');
        navItems.forEach(item => item.classList.add('open'));

        showMenu = true;
    } else {
        hamburger.classList.remove('open');
        nav.classList.remove('open');
        menuNav.classList.remove('open');
        navItems.forEach(item => item.classList.remove('open'));

        showMenu = false;
    }

}


select.onclick = function() {
    console.log("click");
    list.classList.toggle("open");
}
for(option of options){
    option.onclick = function(){
        selectText.innerHTML = this.innerHTML;
        inputField.placeholder = "Search In " + selectText.innerHTML;
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const listItems = document.querySelectorAll('#list .options');

    listItems.forEach(function(item) {
        item.addEventListener('click', function() {
            const manufacturerName = this.dataset.name;
            document.getElementById('selectedManufacturer').value = manufacturerName;
            document.getElementById('manufacturerForm').submit();
        });
    });
});

function validateForm() {
    var selectedManufacturer = document.getElementById('selectText').innerText.trim();
    if (selectedManufacturer === 'All Manufacturers') {
        alert("Please select a manufacturer.");
        return false;
    }
    return true;
}

document.getElementById('list').addEventListener('click', function(event) {
    var selectedOption = event.target.innerText;
    document.getElementById('selectText').innerText = selectedOption;
    document.getElementById('submitBtn').disabled = false;
});
