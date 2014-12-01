(function($, window, document) {
  $(function(){
    var lastParagraph = $('#about p:last-child()')
    var aboutHeader = $('#about h2')
    aboutHeader.on('click', function(event){
      lastParagraph.toggle()
    })
  });
}(window.jQuery, window, document));
