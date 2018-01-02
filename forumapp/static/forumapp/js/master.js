document.addEventListener('DOMContentLoaded', function() {
    chars_left = document.getElementById('chars_left');
    message_field = document.getElementsByTagName('textarea')[0];
    displayCurrentAndMaxLength();

    function displayCurrentAndMaxLength() {
        chars_left.innerText = '' + message_field.textLength + '/' + message_field.maxLength;
    }

    message_field.addEventListener(
        'input', displayCurrentAndMaxLength
    );
});

