var currentpage = Window.location.herf;
// check which page is currently active and set the corresponding link as active
if(currentpage.include("services")){
        document.getElementById("services").classList.add("active");
}else{
        document.getElementById('home').classList.add("active");
}