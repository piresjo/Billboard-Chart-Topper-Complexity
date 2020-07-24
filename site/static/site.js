function scrollFunction() 
{
    var navbarElement = document.getElementsByClassName("navbar")[0];
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) 
    {
        navbarElement.style.top = "0";
    } 
    else 
    {
        navbarElement.style.top = "-50px";
    }
}