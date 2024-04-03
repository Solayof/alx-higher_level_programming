$(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (resp, status) {
    if (status === 'success') {
      $('DIV#hello').text(resp);
    }
  });
});
