from colors import colors,colors_args_kwargs

def test_all_positional():
    result = colors('red', 'blue', 'yellow', 'chartreuse')
    assert 'red' in result
    assert 'blue' in result
    assert 'chartreuse' in result

def test_all_keyword():
    result = colors(link_color='red', back_color='blue')
    assert 'link_color=red' in result
    assert 'back_color=blue' in result

def test_pos_key():
    result = colors('purple', link_color='red', back_color='blue')
    assert 'purple' in result
    assert 'link_color=red' in result
    assert 'back_color=blue' in result

def test_args_kwargs():
    pos_args, key_args = colors_args_kwargs(1,2,3, link_color='blue', visited_color='cyan')
    assert key_args == {'link_color':'blue', 'visited_color':'cyan'}   
    assert pos_args == (1,2,3)


def test_args():
    pos_args, key_args = colors_args_kwargs('red', 'blue', 'yellow', 'chartreuse')
    assert not key_args
    assert pos_args == ('red', 'blue', 'yellow', 'chartreuse')

def test_kwargs():
    pos_args, key_args = colors_args_kwargs(link_color='purple')
    assert not pos_args
    assert key_args == {'link_color':'purple'}
 
def test_args_tup():
    t = ('red', 'blue', 'yellow', 'chartreuse')
    pos_args, key_args = colors_args_kwargs(*t)
    assert not key_args
    assert pos_args == ('red', 'blue', 'yellow', 'chartreuse')

def test_kwargs_dict():
    d = {'fore_color': 'red',
         'visited_color': 'cyan',
         'link_color': 'green',
         'back_color': 'blue',
         }
    pos_args, key_args = colors_args_kwargs(**d)
    assert not pos_args
    assert key_args == {'fore_color': 'red',
                        'visited_color': 'cyan',
                        'link_color': 'green',
                        'back_color': 'blue',}

def test_both_args_kwargs():
    t = ('red', 'blue')
    d = {'visited_color': 'cyan',
        'link_color': 'green',
        }
    pos_args, key_args = colors_args_kwargs(*t, **d)
    assert pos_args == ('red', 'blue')
    assert key_args == {'visited_color': 'cyan',
                        'link_color': 'green'}

def test_mix_args_kwargs():
    t = ('red',)  
    d = {'visited_color': 'cyan'}
    pos_args, key_args = colors_args_kwargs('blue', *t, link_color='orange', **d)
    assert pos_args == ('blue','red')
    assert key_args == {'link_color':'orange','visited_color': 'cyan'}