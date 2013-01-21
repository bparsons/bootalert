# PKGBUILD 
#
# Boot Alert Script Arch Linux Package Build
# 
# Brian Parsons <brian@pmex.com>
#

pkgver=3.1
pkgrel=1
pkgname='bootalert'
pkgdesc='Sends email on system boot'
arch=('any')
backup=('etc/conf.d/bootalert')
depends=('python2' 'postfix')
license=('MIT')
source=('bootalert'
        'bootalert.py'
        'bootalert.service')
md5sums=('eaac18cb46a9baf0117bd3d0cc1cc1c3'
         'd0a3f1917fb727732955ff66d67deced'
         'b56fc4cd1fa06420afad807ab1ec7eaa')

package() {

	install -Dm 600 ${srcdir}/bootalert ${pkgdir}/etc/conf.d/bootalert
	install -Dm 700 ${srcdir}/bootalert.py ${pkgdir}/usr/local/bin/bootalert.py
        install -Dm 655 ${srcdir}/bootalert.service ${pkgdir}/usr/lib/systemd/system/bootalert.service

        mkdir ${pkgdir}/etc/systemd
        mkdir ${pkgdir}/etc/systemd/system
        mkdir ${pkgdir}/etc/systemd/system/multi-user.target.wants
        ln -s /usr/lib/systemd/system/bootalert.service ${pkgdir}/etc/systemd/system/multi-user.target.wants/bootalert.service

}
