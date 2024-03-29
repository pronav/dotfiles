config.load_autoconfig(False)
config.set('tabs.max_width', 320)
config.set('content.notifications.enabled', False)
config.set('colors.webpage.darkmode.enabled', True)
config.set('tabs.title.format', '{index}: {current_title}')

config.unbind('H')
config.unbind('L')
config.unbind('tsu')
config.unbind('tsh')
config.unbind('tpu')
config.unbind('tph')
config.unbind('tiu')
config.unbind('tih')
config.unbind('tcu')
config.unbind('tch')
config.unbind('r')
config.unbind('tcH')
config.unbind('tiH')
config.unbind('tpH')
config.unbind('tsH')
config.unbind('tCh')
config.unbind('tCu')
config.unbind('tCH')
config.unbind('tIh')
config.unbind('tIu')
config.unbind('tIH')
config.unbind('tPH')
config.unbind('tPh')
config.unbind('tPu')
config.unbind('tSu')
config.unbind('tSh')
config.unbind('tSH')
config.unbind('th')
config.unbind('tl')
config.unbind('wh')
config.unbind('wl')
config.unbind('<Alt-m>')
config.bind('<Alt-Right>', 'forward')
config.bind('<Alt-Left>', 'back')
config.bind('<Ctrl-m>', 'tab-mute')

config.unbind('M')
config.unbind('Sq')
config.unbind('Sh')
config.unbind('m')
config.bind('<Ctrl-d>', 'bookmark-add')
config.bind('<Ctrl-b>', 'bookmark-list')
config.bind('<Ctrl-h>', 'history')

config.unbind('<Ctrl-Tab>')
config.unbind('<Ctrl-PgDown>')
config.unbind('<Ctrl-PgUp>')
config.unbind('<Ctrl-Shift-Tab>')
config.unbind('J')
config.unbind('K')
config.bind('<Ctrl-Tab>', 'tab-next')
config.bind('<Ctrl-Shift-Tab>', 'tab-prev')

config.unbind('<Ctrl-Alt-p>')
config.bind('<Ctrl-p>', 'print')

config.unbind('wIf')
config.unbind('wi')
config.bind('<F12>', 'devtools')

config.unbind('q')
config.unbind('@')
config.unbind('ad')
config.unbind('gd')
config.unbind('cd')
config.unbind('.')
config.unbind('sf')
config.unbind('Ss')
config.unbind('gC')
config.unbind('d')
config.unbind('T')
config.unbind('gD')
config.unbind('gm')
config.unbind('G')
config.unbind('ZQ')
config.unbind('co')
config.unbind('u')
config.unbind('gf')
config.unbind('yy')
config.unbind('<Ctrl-q>')

config.unbind('n')
config.unbind('N')
config.bind('<Down>', 'search-next')
config.bind('<Up>', 'search-prev')
config.bind('<Left>', 'search-prev')
config.bind('<Right>', 'search-next')

config.unbind('=')
config.unbind('+')
config.unbind('-')
config.bind('<Ctrl-=>', 'zoom-in')
config.bind('<Ctrl-->', 'zoom-out')
config.bind('<Ctrl-0>', 'zoom 100')
