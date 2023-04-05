isR=0
[ -f /tmp/base.en.lmo ] && {
	[ "$(mount| grep '/usr/lib/lua/luci/i18n')" == "" ] || umount /usr/lib/lua/luci/i18n
	[ -f /usr/lib/lua/luci/i18n/base.en.lmo ] || {
		mv /tmp/base.en.lmo /etc/base.en.lmo
		[ "$(grep 'base.en.lmo' /etc/rc.local)" == "" ] && {
			echo "[ -f /usr/lib/lua/luci/i18n/base.en.lmo ] && exit" > /etc/rc.l
			echo "mkdir /tmp/i18n" >> /etc/rc.l
			echo "cp /usr/lib/lua/luci/i18n/* /tmp/i18n" >> /etc/rc.l
			echo "cp /etc/base.en.lmo /tmp/i18n" >> /etc/rc.l
			echo "mount --bind /tmp/i18n /usr/lib/lua/luci/i18n" >> /etc/rc.l
			cat /etc/rc.local >> /etc/rc.l
			rm /etc/rc.local
			mv /etc/rc.l /etc/rc.local
			chmod +x /etc/rc.local
			/etc/rc.local
			isR=1
		} || {
			cp /etc/base.en.lmo /tmp/i18n
			mount --bind /tmp/i18n /usr/lib/lua/luci/i18n
		}
	}
}
isC=0
if [ -f /usr/lib/lua/luci/i18n/base.en.lmo ] || [ -f /etc/base.en.lmo ]; then
	[ "$(uci get luci.main.lang)" == "en" ] || {
		uci set luci.main.lang=en
		isC=1
	}
	[ "$(uci get luci.languages.en)" == "English" ] || {
		uci set luci.languages.en=English
		isC=1
	}
	[ $isC -eq 1 ] && {
		uci commit luci
		isR=1
	}
	[ $isC -eq 1 ] && /etc/init.d/sysapihttpd restart
fi

