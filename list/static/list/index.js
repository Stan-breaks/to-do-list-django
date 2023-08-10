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
function mark_task(event){
fetch(event.target.dataset.url,{
    method:'POST',
    body:JSON.stringify({
        done:true
    })
})
.then(response=>response.json())
.then(response=>{
    console.log(response)
    location.reload()
})
}
function delete_task(event){
var taskContainer=event.target.parentElement;
 taskContainer.style.animationPlayState='running';
 taskContainer.addEventListener('animationend',()=>{
  taskContainer.remove()  
  fetch(event.target.dataset.url,{
    method:'POST',
    body:JSON.stringify({
        delete:true
    })
  })
  .then(response=>response.json())
  .then(response=>{
    console.log(response)
    location.reload()
  })
 });
}