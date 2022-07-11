//$(document).ready(function(){
//
//  cookiesPolicyBar();
//});
//
//function cookiesPolicyBar(){
//    // Check cookie
//    if (getCookie('mtm_consent') != "active") $('#cookieAcceptBar').show();
//    //Assign cookie on click
//    $('#cookieAcceptBarConfirm').on('click',function(){
//        setCookie('mtm_consent', 'active', 7); // cookie will expire in seven days
//        $('#cookieAcceptBar').fadeOut();
//    });
//}
//
//function setCookie(cname, cvalue, exdays) {
//  const d = new Date();
//  d.setTime(d.getTime() + (exdays * 24 * 60 * 60 * 1000));
//  let expires = "expires="+d.toUTCString();
//  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
//}
//
//function getCookie(cname) {
//  let name = cname + "=";
//  let ca = document.cookie.split(';');
//  for(let i = 0; i < ca.length; i++) {
//    let c = ca[i];
//    while (c.charAt(0) == ' ') {
//      c = c.substring(1);
//    }
//    if (c.indexOf(name) == 0) {
//      return c.substring(name.length, c.length);
//    }
//  }
//  return "";
//}
//
//function checkCookie() {
//  let user = getCookie("username");
//  if (user != "") {
//    alert("Welcome again " + user);
//  } else {
//    user = prompt("Please enter your name:", "");
//    if (user != "" && user != null) {
//      setCookie("username", user, 365);
//    }
//  }
//}
//
//

const cookieStorage = {
    getItem: (item) => {
        const cookies = document.cookie
            .split(';')
            .map(cookie => cookie.split('='))
            .reduce((acc, [key, value]) => ({ ...acc, [key.trim()]: value }), {});
        return cookies[item];
    },
    setItem: (item, value) => {
        document.cookie = `${item}=${value};`
    }
}

const storageType = cookieStorage;
const consentPropertyName = 'jdc_consent';
const shouldShowPopup = () => !storageType.getItem(consentPropertyName);
const saveToStorage = () => storageType.setItem(consentPropertyName, true);

window.onload = () => {

    const acceptFn = event => {
        saveToStorage(storageType);
        consentPopup.classList.add('hidden');
    }
    const consentPopup = document.getElementById('consent-popup');
    const acceptBtn = document.getElementById('accept');
    acceptBtn.addEventListener('click', acceptFn);

    if (shouldShowPopup(storageType)) {
        setTimeout(() => {
            consentPopup.classList.remove('hidden');
        }, 2000);
    }

};