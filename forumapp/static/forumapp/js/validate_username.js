function validate_username(validation_url) {
    $('#id_username').change(function() {
        const username = $(this).val();
        const username_field = $('#id_username');

        $.ajax({
            url: validation_url,
            data: {
                'username': username
            },
            dataType: 'json',
            success: function(data) {
                if(data.is_taken){
                    username_field.removeClass('is-valid');
                    username_field.addClass('is-invalid');
                    $("#submit").prop('disabled', true);
                } else {
                    username_field.removeClass('is-invalid');
                    username_field.addClass('is-valid');
                    $("#submit").prop('disabled', false);
                }
            }
        });
    });
}
