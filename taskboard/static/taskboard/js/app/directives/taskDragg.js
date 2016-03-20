app.directive('taskDragg', function () {
   return {
       link: function ($scope, element, attrs) {

           var dragData = "";
           $scope.$watch(attrs.taskDragg, function (newValue) {
               dragData = newValue;
           });

           element.bind('dragstart', function (event) {
               event.originalEvent.dataTransfer.setData("Text", JSON.stringify(dragData));
           });
       }
   };
});