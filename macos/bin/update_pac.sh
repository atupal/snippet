#! /bin/sh -u

#Ref: https://www.google.com.hk/search?newwindow=1&dcr=0&source=hp&ei=bHE2WpyLN8Ks0ASeqYTQBA&q=mac+os+networksetup+pac&oq=mac+os+networksetup+pac&gs_l=psy-ab.3..33i160k1l3.1117.9351.0.9994.31.19.6.0.0.0.299.2556.2j8j5.15.0....0...1.1.64.psy-ab..10.21.2593.0..0j0i131k1j0i10k1j0i22i30k1j0i22i10i30k1j0i8i13i30k1j33i22i29i30k1.0.trniArJaLzY
#     https://q1f4mmprz7gko.wordpress.com/2015/07/10/forcing-mac-os-x-and-safari-to-reload-a-pac-file/

networksetup -listallnetworkservices | awk 'NR>1' | while read SERVICE ; do
  if networksetup -getautoproxyurl "$SERVICE" | grep '^Enabled: Yes' >/dev/null; then
    networksetup -setautoproxystate "$SERVICE" off
    networksetup -setautoproxystate "$SERVICE" on
    echo "$SERVICE" bounced.
  fi
done
