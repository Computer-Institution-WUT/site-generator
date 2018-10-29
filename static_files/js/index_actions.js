function change_select(_targ) {
  if (_targ === 'bing') {
    $('#show_button')[0].innerText = 'Bing';
    _current = 'bing'
  } else if (_targ === 'rar') {
    $('#show_button')[0].innerText = 'RARBG';
    _current = 'rar'
  } else if (_targ === 'subhd') {
    $('#show_button')[0].innerText = 'SubHD';
    _current = 'subhd'
  } else if (_targ === 'cilimao') {
    $('#show_button')[0].innerText = 'Cilimao';
    _current = 'cilimao'
  }
}

function make_search() {
  var _string = $('#search_string')[0].value;
  if (_current === 'bing') {
    window.open("https://cn.bing.com/search?q=" + _string);   
  } else if (_current === 'rar') {
    window.open("https://rarbg.is/torrents.php?search=" + _string);  
  } else if (_current === 'subhd') {
    window.open("http://subhd.com/search0/" + _string);  
  } else if (_current === 'cilimao') {
    window.open("http://www.cilimao.me/search?word=" + _string + "&page=1" + _string);  
  }
}

function clear_search() {
  $('#search_string')[0].value = '';
}
