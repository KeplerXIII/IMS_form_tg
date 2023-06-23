let tg = window.Telegram.WebApp
let orderBtn = document.getElementById('order')
tg.expand();

// buyBtn.addEventListener('click', () => {
//     document.getElementById('main').style.display = 'none'
//     document.getElementById('form').style.display = 'block'
//     // document.getElementById('user_name').value = tg.initDataUnsafe.user.first_name + ' ' + tg.initDataUnsafe.user.last_name
// })

orderBtn.addEventListener('click', (e) => {
    e.preventDefault()
    document.getElementById('error').innerText = ''
    let name = document.getElementById('user_name').value
    let email = document.getElementById('user_email').value
    let phone = document.getElementById('user_phone').value
    let text = document.getElementById('user_text').value

    if(name.length < 5) {
        document.getElementById('error').innerText = 'Введите имя'
        return
    }

    if(email.length < 5) {
        document.getElementById('error').innerText = 'Введите email'
        return
    }

    if(phone.length < 5) {
        document.getElementById('error').innerText = 'Введите телефон'
        return
    }

    if(text.length < 5) {
        document.getElementById('error').innerText = 'Поле обращение не должно быть пустым'
        return
    }
    
    let data = {
        name: name,
        email: date,
        phone: phone,
        text: text
    }

    tg.sendData(JSON.stringify(data))
    tg.close()

    console.log(data)
})