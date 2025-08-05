function setMsgAnimation(msgBox){
    if(msgBox){
        msgBox.style.animation = 'fadeOut 3.5s ease-in forwards'
        setTimeout(()=>{
            msgBox.style.animation = '';
            msgBox.remove();
        }, 3501);
    }
}

document.addEventListener('DOMContentLoaded', ()=>{
    const msgBoxes = document.querySelectorAll('.msg-box');
    msgBoxes.forEach(msg=>{
        setMsgAnimation(msg);
    })
})

export function displayMessage(msg, type){
    const main = document.getElementsByTagName('main')[0];
    const span = document.createElement('span');
    span.classList.add("msg-box", type);
    const i = document.createElement('i');
    const message = document.createElement('p');
    
    if (type === 'success') {
        i.classList.add('bi', 'bi-check-square')
    } else {
        i.classList.add('bi', 'bi-exclamation-octagon');
    }
    

    if(type === 'error'){
        if(window.location.pathname === "/cadastro/"){
            let listErrors = Object.entries(msg).map(part => part[1][0]);
            console.log(listErrors);
            
            listErrors.forEach(erroMsg=>{
                message.innerHTML+=`${erroMsg}<br>`;
            })
        }else{
            message.textContent = msg;
        }

    }else{
        console.log(msg);
        message.textContent = msg;
    }
    span.appendChild(i);
    span.appendChild(message);
    main.appendChild(span);

    setMsgAnimation(span);
}
