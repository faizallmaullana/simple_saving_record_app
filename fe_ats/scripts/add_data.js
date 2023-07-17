
$(document).ready(function() {
    $('#inputForm').submit(function(event) {
        event.preventDefault();

        var form = $(this);
        var url = form.attr('action');
        var method = form.attr('method');
        var data = {
            amount: form.find('input[name="income"]').val(),
            description: form.find('input[name="keterangan"]').val()
        };

        fetch(url, {
            method: method,
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        })
        // .then(response => response.json())
        .then(result => {
            alert(result.message);
            form.trigger('reset');
        })
        .catch(error => console.log(error));
    });
});
