$(function () {
  $('INPUT#btn_translate').click(function () {
    $.get('https://www.fourtonfish.com/hellosalut/hello/' + $('INPUT#language_code').val() + '?format=json', function (resp, status) {
      if (status === 'success') {
        $('DIV#hello').text(resp.hello);
      }
    });
  });
});
