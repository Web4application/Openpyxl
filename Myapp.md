name: myapp
version: 23.3.25
summary: KDE MyApp packaged as Snap
description: |
  MyApp is a KDE application built with KDE Neon frameworks, packaged as a Snap.
grade: stable
confinement: strict
base: core22

apps:
  myapp:
    command: desktop-launch $SNAP/usr/bin/myapp
    common-id: org.kde.myapp.desktop
    plugs:
      - home
      - network
      - network-bind
      - audio-playback
      - removable-media
      - desktop
      - opengl
      - wayland
      - x11

plugs:
  desktop:
    mount-host-font-cache: false
  icon-themes:
    interface: content
    target: $SNAP/data-dir/icons
    default-provider: gtk-common-themes
  sound-themes:
    interface: content
    target: $SNAP/data-dir/sounds
    default-provider: gtk-common-themes
  kf5:
    content: kf5-5-104-qt-5-15-8-core22-all
    interface: content
    default-provider: kf5-5-104-qt-5-15-8-core22
    target: $SNAP/kf5

environment:
  SNAP_DESKTOP_RUNTIME: $SNAP/kf5

hooks:
  configure:
    plugs:
      - desktop
      - icon-themes
      - sound-themes
    command-chain:
      - snap/command-chain/hooks-configure-desktop

layout:
  /usr/share/X11:
    symlink: $SNAP/kf5/usr/share/X11

slots:
  session-dbus-interface:
    interface: dbus
    name: org.kde.myapp
    bus: session

package-repositories:
  - type: apt
    suites: [jammy]
    components: [main]
    url: http://origin.archive.neon.kde.org/user
    key-server: keyserver.ubuntu.com
    key-id: 444DABCF3667D0283F894EDDE6D4736255751E5D

parts:
  kde-neon:
    source: /snap/snapcraft/current/share/snapcraft/extensions/desktop/kde-neon
    source-type: local
    plugin: make
    make-parameters:
      - PLATFORM_PLUG=kf5-5-106-qt-5-15-9-core22
    build-snaps:
      - kf5-5-106-qt-5-15-9-core22-sdk
    build-environment:
      - PATH: /snap/kf5-5-106-qt-5-15-9-core22-sdk/current/usr/bin${PATH:+:$PATH}
      - XDG_DATA_DIRS: $CRAFT_STAGE/usr/share:/snap/kf5-5-106-qt-5-15-9-core22-sdk/current/usr/share:/usr/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}
      - XDG_CONFIG_HOME: $CRAFT_STAGE/etc/xdg:/snap/kf5-5-106-qt-5-15-9-core22-sdk/current/etc/xdg:/etc/xdg${XDG_CONFIG_HOME:+:$XDG_CONFIG_HOME}
      - CRAFT_CMAKE_ARGS: -DCMAKE_FIND_ROOT_PATH=/snap/kf5-5-104-qt-5-15-8-core22-sdk/current${CRAFT_CMAKE_ARGS:+:$CRAFT_CMAKE_ARGS}

  myapp:
    plugin: cmake
    source: ../myapp       # Local path to your working source
    after:
      - kde-neon
    parse-info:
      - usr/share/metainfo/org.kde.myapp.appdata.xml
    build-packages:
      - libkf5doctools-dev
    stage-packages:
      - kio
    cmake-parameters:
      - "-DCMAKE_INSTALL_PREFIX=/usr"
      - "-DCMAKE_BUILD_TYPE=Release"
      - "-DENABLE_TESTING=OFF"
      - "-DBUILD_TESTING=OFF"
      - "-DKDE_SKIP_TEST_SETTINGS=ON"
      - "-DCMAKE_FIND_ROOT_PATH=/usr:$CRAFT_STAGE:/snap/kf5-5-104-qt-5-15-8-core22-sdk/current"
      - "-DKDE_INSTALL_PLUGINDIR=/usr/lib/$CRAFT_ARCH_TRIPLET/qt5/plugins/"
    prime:
      # Keep only what is required for your app
      - usr/bin/myapp
      - usr/lib/*/qt5/plugins
      - usr/lib/*/kf5
      - usr/share/icons/breeze*
      - usr/share/metainfo
      - usr/share/applications
      # Exclude unnecessary files
      - "!usr/share/doc/*"
      - "!usr/share/man/*"
      - "!usr/include/*"
      - "!usr/lib/gcc/*"
      - "!usr/lib/aspell/*"
    build-environment:
      - PATH: /snap/kf5-5-106-qt-5-15-9-core22-sdk/current/usr/bin${PATH:+:$PATH}
      - XDG_DATA_DIRS: $CRAFT_STAGE/usr/share:/snap/kf5-5-106-qt-5-15-9-core22-sdk/current/usr/share:/usr/share${XDG_DATA_DIRS:+:$XDG_DATA_DIRS}
      - XDG_CONFIG_HOME: $CRAFT_STAGE/etc/xdg:/snap/kf5-5-106-qt-5-15-9-core22-sdk/current/etc/xdg:/etc/xdg${XDG_CONFIG_HOME:+:$XDG_CONFIG_HOME}
      - CRAFT_CMAKE_ARGS: -DCMAKE_FIND_ROOT_PATH=/snap/kf5-5-104-qt-5-15-8-core22-sdk/current${CRAFT_CMAKE_ARGS:+:$CRAFT_CMAKE_ARGS}

  cleanup:
    after:
      - kde-neon
      - myapp
    plugin: nil
    override-prime: |
      set -eux
      # Remove leftover unnecessary files to shrink Snap size
      rm -rf $SNAP/usr/share/doc/*
      rm -rf $SNAP/usr/share/man/*
      rm -rf $SNAP/usr/include/*
      rm -rf $SNAP/usr/lib/gcc/*
      rm -rf $SNAP/usr/lib/aspell/*
      rm -rf $SNAP/usr/share/lintain