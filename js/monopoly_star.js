$('#service-msg-wrapper').remove();
for (let step = 0; step < 500; step++) {
  setTimeout(function() {var message = 'YOUR MESSAGE HERE!';
    playField.sendMessage(message);playField.throwDices();},200)
}