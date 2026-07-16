# Music-game and mobile-game backup findings

Search date: 2026-07-16

The thematic search inspected 401 unique Internet Archive items. It identified 130 useful backup/data candidates and 89 game-related candidates. The search queries returned 77 results for `rhythm game` combined with backup, emulator or snapshot terms, and 40 results for `music game` with those terms. Many results were false positives, videos or music albums, so file lists and descriptions were inspected before classification.

## sifas_jp

Internet Archive item: `https://archive.org/details/sifas_jp`

Title: Love Live! School Idol Festival ALL STARS JP Game Assets.

The uploader describes this as a backup of all assets available in the Japanese release up to 2023-06-24, before discontinuation on 2023-06-30. The item includes `masterdata.db`, asset databases, dictionary databases and thousands of package files under `original/files/pkg0`. This is a verified example of a discontinued mobile rhythm game's downloaded asset directory being preserved directly rather than as an emulator snapshot.

## bbvp_20251226

Internet Archive item: `https://archive.org/details/bbvp_20251226`

Title: Beat Beat Vocaloid Plus 1.8.18 and data files. The item contains the APK and a 171,921,886-byte `KGS.7z` data archive. The uploader notes that the data is incomplete, although some songs are playable.

## OverrapidServerBackup

Internet Archive item: `https://archive.org/details/OverrapidServerBackup`

Title: OverRapid Server download backup. The page says it will remain dormant until the game server shuts down. At the time of inspection it contained only Internet Archive metadata/torrent files and no game payload, so it is a monitoring target rather than a usable backup.

## Other useful patterns

The search also found projects that publish multiple importable emulator environments under a shared identifier prefix, such as the `rr-3-armageddon-v-` Real Racing 3 preservation series. This supports searching by uploader, project name, file extension and description phrases rather than only by exact game title.