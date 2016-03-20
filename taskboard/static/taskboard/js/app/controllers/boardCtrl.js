app.controller('boardCtrl', function ($scope, boardService) {
    // Model
    $scope.columns = [];

    function init() {
        $scope.refreshBoard();
        var ws_url = "ws://127.0.0.1:8000/ws/tasks?subscribe-broadcast";
        var ws = new WebSocket(ws_url);
        ws.onopen = function (evt) {
            console.log('Connected');
        };
        ws.onclose = function (evt) {
            console.log('Disconnected');
            $timeout(function () {
                ws.connect(ws_url);
            }, 1000);
        };
        ws.onerror = function (evt) {
            console.error('Websocket connection is broken!');
            ws.close();
        };
        ws.onmessage = function (evt) {
            try {
                var data = angular.fromJson(evt.data);
            } catch (e) {
                console.warn('Data received by server is invalid JSON: ' + evt.data);
                return;
            }
            console.log(data);
            if (data.update) {
               $scope.refreshBoard();
            }
        };
    }

    $scope.refreshBoard = function refreshBoard() {
        boardService
            .getColumns()
            .then(function (data) {
                $scope.columns = data;
            }, onError);
    };

    $scope.onDrop = function (data, targetColId) {
        boardService.moveTask(data, targetColId).then(function (taskMoved) {
            if (taskMoved) {
                $scope.refreshBoard();
            }
        }, onError);
    };

    // Listen to the 'refreshBoard' event and refresh the board as a result
    $scope.$parent.$on("refreshBoard", function (e) {
        $scope.refreshBoard();
        toastr.success("Board updated successfully", "Success");
    });

    var onError = function (errorMessage) {
        toastr.error(errorMessage, "Error");
    };

    init();

});
