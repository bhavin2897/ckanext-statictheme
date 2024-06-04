if ( $('.cookie-wrapper').length > 0 ) {

const cookieBox = document.querySelector(".cookie-wrapper"),
acceptBtn = cookieBox.querySelector("button");

//declineBtn = document.querySelector(".decline");
//
//declineBtn.onclick = ()=>{
//  console.log("declinebtn");
//  document.cookie = "nfdi4chem=active; max-age="+60*60*24*30;
//  if(document.cookie){
//  //if cookie is set
//  }
//  else{
//  //if cookie not set then alert an error
//    cookieBox.classList.add("hide"); //hide cookie box
//  }
//}



acceptBtn.onclick = ()=>{
   console.log("acceptbtn");
  //setting cookie for 1 month, after one month it'll be expired automatically
  document.cookie = "nfdi4chem=active; max-age="+60*60*24*30;
  if(document.cookie){ //if cookie is set
    cookieBox.classList.add("hide"); //hide cookie box
  }else{ //if cookie not set then alert an error
    alert("Cookie can't be set! Please unblock this site from the cookie setting of your browser.");
  }
}

let checkCookie = document.cookie.indexOf("nfdi4chem=active"); //checking our cookie
//if cookie is set then hide the cookie box else show it
checkCookie != -1 ? cookieBox.classList.add("hide") : cookieBox.classList.remove("hide");

}
