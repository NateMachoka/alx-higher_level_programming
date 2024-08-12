$(document).ready(function() {
    $('#btn_translate').click(function() {
        // Get the value of the input field
        var langCode = $('#language_code').val();
        // Perform an AJAX GET request to fetch the translation
        $.get('https://www.fourtonfish.com/hellosalut/hello/', { lang: langCode }, function(data) {
            // Update the content of DIV#hello with the fetched translation
            $('#hello').text(data.hello);
        }).fail(function() {
            // Handle errors, if any
            $('#hello').text('Error fetching translation');
        });
    });
});
