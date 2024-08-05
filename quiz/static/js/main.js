$('.btn').click(function() {
    // продумать для карточек, которые не должны переворачиваться
    var card = $(this).parent().parent('.card');
    var cardReg = card.next();
    if (!$(this).hasClass('btn-reg') && !$(this).hasClass('btn-join')) {
        $('.card__close').trigger('click');
    }
    card.css('transform', 'perspective(600px) rotateY(-180deg)');
    cardReg.css('transform', 'perspective(600px) rotateY(0deg)');
});

$('.card__close').click(function() {
    var card = $(this).parent('.card');
    if (card.hasClass('card--done')) {
        var cardReg = card.prev().prev();
    } else {
        var cardReg = card.prev();
    }
    card.css('transform', 'perspective(600px) rotateY(180deg)');
    cardReg.css('transform', 'perspective(600px) rotateY(0deg)');
});

$('.menu__auth').click(function() {
    $('.modal--auth').addClass('modal--visible');
});

$('.modal__close').click(function() {
    $('.modal').removeClass('modal--visible');
    // сбрасывать формы
    $('#form-reg')[0].reset();
    $('#form-auth')[0].reset();
});

$('.form__reg').click(function() {
    $('.modal--auth').removeClass('modal--visible');
    $('.modal--reg').addClass('modal--visible');
});

$('.btn--reg').click(function(e) {
    e.preventDefault();
    var pass1 = $('.pass1').val();
    var pass2 = $('.pass2').val();
    var name = $('.name').val();
    var mail = $('#reg-mail').val();
    var admin = $('#admin').prop('checked');

    // не забыть проверку на пустоту

    if (pass1 != pass2) { // совпадение паролей
        $('.form__error').css('visibility', 'visible');
    }

    $.ajax({
        url: '/ajax/',
        method: 'post',
        dataType: 'JSON',
        data: {
            'ajax': 'reg',
            'name': name,
            'mail': mail,
            'pass': pass1,
            'admin': admin
        },
        success: function(data) {
            if (data['status'] == 'Дубликат почты') {
                $('.form__error').text('Ошибка! Пользователь с таким адресом почты уже существует');
                $('.form__error').css('visibility', 'visible');
                $('.form__error').css('color', 'red');
            } else if (data['status'] == 'Ошибка' || data['status'] == undefined) {
                $('.form__error').text('Возникла ошибка, попробуйте позже');
                $('.form__error').css('visibility', 'visible');
                $('.form__error').css('color', 'red');
            } else {
                $('.form__error').text('Вы успешно зарегистрированы');
                $('.form__error').css('visibility', 'visible');
                $('.form__error').css('color', 'green');
            }
        },
        error: function(data) {
            $('.form__error').text('Возникла ошибка, попробуйте позже');
        }
    });
});

$('.btn--auth').click(function(e) {
    e.preventDefault();
    var mail = $('.mail').val();
    var pass = $('.pass').val();
    if (mail == '' || pass == '') {
        $('.auth-error').css('display', 'block');
    } else {
        $.ajax({
            url: '/ajax/',
            method: 'post',
            dataType: 'JSON',
            data: {
                'ajax': 'auth',
                'mail': mail,
                'pass': pass,
            },
            success: function(data) {
                alert('OK');
                console.log(data);
                // получить сессию, добавить в index input hidden, открыть нужные поля
            },
            error: function(data) {
                $('.auth-error').text('Возникла ошибка, попробуйте позже');
                $('.auth-error').css('display', 'block');
            }
        });
    }
});

$('#form-auth input').on('change', function() {
    $('.auth-error').css('display', 'none');
})

$('.menu__actions').click(function(e) {
    $('.left-menu').css('display', 'block');
    // в зависимости от роли открывать необходимую
    // либо предусмотреть сразу подгрузку необходимой в index.html (этот вариант лучше)
    $('.left-menu__admin').css('display', 'block');
});

$('.menu__people').click(function(e) {
    $('.left-menu-data').css('display', 'block');
});

$('.left-menu__close').click(function(e) {
    $('.left-menu').css('display', 'none');
});

$('.left-menu-data__close').click(function(e) {
    $('.left-menu-data').css('display', 'none');
});

$('.btn-qs').click(function() {
    $('.quiz').css('display', 'none');
    $('.questions').css('display', 'flex');
    $(this).addClass('btn--active');
    $('.btn-info').removeClass('btn--active');
});

$('.btn-info').click(function() {
    $('.quiz').css('display', 'block');
    $('.questions').css('display', 'none');
    $(this).addClass('btn--active');
    $('.btn-qs').removeClass('btn--active');
});
