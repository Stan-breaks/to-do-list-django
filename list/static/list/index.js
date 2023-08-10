function add(event){
    event.preventDefault();
    fetch(event.target.dataset.url,{
        method:'POST',
        body:JSON.stringify({
            text:document.querySelector("#text").value
        })
    })
    .then(response=>response.json())
    .then(response=>{
        console.log(response);
        location.reload();
    })
}
function mark_task(){

}
function delete_task(){

}