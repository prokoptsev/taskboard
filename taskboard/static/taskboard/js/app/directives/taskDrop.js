app.directive('taskDrop', function () {
   return {
       link: function ($scope, element, attrs) {

           var dragOverClass = attrs.taskDrop;

           //  Prevent the default behavior. This has to be called in order for drob to work
           cancel = function (event) {
               if (event.preventDefault) {
                   event.preventDefault();
               }

               if (event.stopPropigation) {
                   event.stopPropigation();
               }
               return false;
           };

           element.bind('dragover', function (event) {
               cancel(event);
               event.originalEvent.dataTransfer.dropEffect = 'move';
               element.addClass(dragOverClass);
           });

           element.bind('drop', function (event) {
               cancel(event);
               element.removeClass(dragOverClass);
               var droppedData = JSON.parse(event.originalEvent.dataTransfer.getData('Text'));
               $scope.onDrop(droppedData, element.attr('id'));

           });

           element.bind('dragleave', function (event) {
               element.removeClass(dragOverClass);
           });
       }
   };
});