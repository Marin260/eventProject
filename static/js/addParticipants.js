const btn1 = document.querySelectorAll('.btn-dolazim')
const btn2 = document.querySelectorAll('.btn-zainteresiran')

for(const btns of [btn1, btn2]){
    btns.forEach(btn => {
        btn.addEventListener('click', e => {
            e.preventDefault()
            const id = e.target.getAttribute('data-id')
            const field = e.target.getAttribute('data-field')
            postDolaze(id, parseInt(field))
        })
    })
}

const postDolaze = (id, field) => {
    $.post({
        url: '/addPeopleToEvent/',
        data: {
            eventid: id, //send id
            modelField: field, //send type field
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),//,'{{csrf_token}}'
            action: 'post'
        },
    }).done(json => {
        var htmlField = (field == 1) ? 'dolaze' : 'zainteresirani'
        document.querySelector(`#${htmlField}-${id}`).innerHTML = htmlField + ': ' + json['result']
        console.log(json)
    }).fail()
}