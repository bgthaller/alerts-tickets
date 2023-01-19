

$('#add-alert').on('click', function () {
    $('.form-add-alert').removeClass('hidden')
    $('.form-add-ticket').addClass('hidden')
    
})



$('#add-ticket').on('click', function () {
    $('.form-add-ticket').removeClass('hidden')
    $('.form-add-alert').addClass('hidden')
})

$('#cancel-form').on('click', function () {
    $('.form-add-ticket').addClass('hidden')
    $('.form-add-alert').addClass('hidden')
})