// var dolazeBtn = document.getElementById('add-dolazim').addEventListener('click', function(e){
//     e.preventDefault()
//     console.log('presed')
//     const xhttp = new XMLHttpRequest();
//     xhttp.onload = function() {
        
//         document.getElementById("test").innerHTML = this.responseText;
//     }
//     xhttp.open(
//         'GET',
//         '{% url "dolazim" %}',);
//     xhttp.send();
// })

function addDol(eid, field) {
    //e.preventDefault()
    $.ajax({
        type: 'POST',
        url: '/addPeopleToEvent/',
        data: {
            eventid: eid, //send id
            modelField: field, //send type field
            csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),//,'{{csrf_token}}'
            action: 'post'
        },
        success: function(json){
            var htmlFiled = (field == 1) ? 'dolaze' : 'zainteresirani'
            var htmlId = htmlFiled + '-' + eid
            document.getElementById(htmlId).innerHTML = htmlFiled + ': ' + json['result']
            console.log(json)
        },
        error: function(xhr, errmsg, err){}
    })
}

// $(document).on('click', '#add-dolazim', function(e){
//     e.preventDefault()
//     $.ajax({
//         type: 'POST',
//         url: '/dolazim/',
//         data: {
//             eventid: $('#add-dolazim').val(),
//             csrfmiddlewaretoken: $('input[name="csrfmiddlewaretoken"]').val(),//,'{{csrf_token}}'
//             action: 'post'
//         },
//         success: function(json){
//             document.getElementById('dolaze').innerHTML = 'dolaze: ' + json['result']
//             console.log(json)
//         },
//         error: function(xhr, errmsg, err){}
//     })
// })
