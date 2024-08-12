$(document).ready(function() {
    function fetchTranslation() {
        const languageCode = $('#language_code').val();
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: languageCode }, function(data) {
            $('#hello').text(data.hello);
        });
    }

    // Event handler for button click
    $('#btn_translate').on('click', fetchTranslation);

    // Event handler for ENTER key press
    $('#language_code').on('keypress', function(event) {
        if (event.which === 13) { // 13 is the ENTER key
            fetchTranslation();
        }
    });
});
