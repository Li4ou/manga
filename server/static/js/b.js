function get_cookie(cookie_name) {
    var results = document.cookie.match('(^|;) ?' + cookie_name + '=([^;]*)(;|$)');
    if (results)
        return (unescape(results[2]));
    else
        return null;
}

function showMessage() {
    let ids = localStorage.getItem('recently_viewed');

    if (ids != null) {
        let idss = ids.split([','])
        let url = "api/manga/?id=" + ids;
        $.ajax({
            type: "get",
            url: url,
            success: function (response, ids) { //Данные отправлены успешно
                result = response;
                $('#mangaInterest').append('<div class="card card-body mb-3" >' +
                    '<div class=' + "p-2" + '><b>Вы интересовались</b></div> ' +
                    '                        <div class="px-2">\n' +
                    '                            <div class="hot-media-wrap" id="test2">\n' +


                    '                             </div>' +
                    '</div>'
                );
                idss.forEach(function (item, i) {
                    $('#test2').append(
                        '                                    <div class="hot-media-item media-card-wrap media-card-wrap_sm m-1 "\n' +
                        '                                         style="width: 150px">\n' +
                        '                                        <a href="" title="" class="">\n' +
                        '                                            <img src="' + result[item].poster + '" class=""\n' +
                        '                                                 style="height: 200px"\n' +
                        '                                                 alt="...">\n' +
                        '                                            <div class="w-100 text-center test">' + result[item].title + '\n' +
                        '                                            </div>\n' +
                        '                                        </a>\n'
                    );
                    ;
                });


            }
        })

    }

}

showMessage()
