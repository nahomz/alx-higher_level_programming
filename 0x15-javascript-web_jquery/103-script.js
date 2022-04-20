function sayHello () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('input#language_code').val();
    $.get(url, (data, status) => {
      $('div#hello').text(data.hello);
    });
  }
  
  $(document).ready(() => {
    $('input#btn_translate').click(sayHello);
    $('input#language_code').keypress((event) => {
      const keycode = (event.keycode ? event.keycode : event.which);
      if (keycode === '13') {
        sayHello();
      }
    });
  });
  