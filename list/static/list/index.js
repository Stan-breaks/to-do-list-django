function add(event){
 
    fetch(event.target.dataset.url,{
        method:'POST',
        body:JSON.stringify({
            text:document.querySelector("#text").value
        })
    })
    .then(response=>response.json())
    .then(response=>{
        console.log(response);
    })
    setTimeout(function() {
        location.reload();
    }, 500);
}