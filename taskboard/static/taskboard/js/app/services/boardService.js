app.service('boardService', function ($http, $q, $rootScope) {

    var getColumns = function () {
        return $http.get("/api/v1/board").then(function (response) {
            return response.data;
        }, function (error) {
            return $q.reject(error.data.Message);
        });
    };

    var moveTask = function (taskData, targetColIdVal) {
        return $http.put("/api/v1/tasks/" + taskData.id, {status_id: targetColIdVal, name: taskData.name}).then(function (response) {
            return response.status == 200;
        }, function (error) {
            return $q.reject(error.data.Message);
        });
    };

    return {
        getColumns: getColumns,
        moveTask: moveTask
    };
});
