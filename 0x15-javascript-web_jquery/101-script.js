$(document).ready(function() {
    // Add new <li> element to the list
    $('#add_item').click(function() {
        $('.my_list').append('<li>Item</li>');
    });

    // Remove the last <li> element from the list
    $('#remove_item').click(function() {
        $('.my_list li').last().remove();
    });

    // Clear all <li> elements from the list
    $('#clear_list').click(function() {
        $('.my_list').empty();
    });
});
