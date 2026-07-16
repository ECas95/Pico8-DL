# General Android emulator backup and mobile-game data catalog

Search date: 2026-07-16

## Search scope

The search intentionally did not require SEVEN'S CODE in the title. Internet Archive Advanced Search was queried for BlueStacks, Nox, LDPlayer, MEmu, MuMu, emulator backup/snapshot terms, virtual-disk formats, mobile games, rhythm games, downloaded server files, APK plus data packages, and preserved DLC. The resulting catalog inspected 359 unique Internet Archive items. It found 45 items containing disk-image formats and 119 items matching backup names or game-preservation terms.

## Highest-value public examples

### ff7tfs-nox

Internet Archive item: `https://archive.org/details/ff7tfs-nox`

Title: Final Fantasy VII: The First SOLDIER v1.0.28 (Nox Backup with Server Files).

This is an importable Nox backup containing the final game version and all files downloaded from the former game server. The uploader states that no account is tied to the image. File: `NoxPlayerwithFirstSoldier1028 - Server Downloaded.npbk`, 8,042,662,904 bytes, MD5 `61b4cac793094d989bf62a62a8048bb0`, SHA-1 `85377eb8cc02f73dbcb199635b74abc5e6f478ff`.

### RR3 Armageddon series

Example item: `https://archive.org/details/rr-3-armageddon-v-8.5.0`

Project Armageddon publishes importable NoxPlayer and VPhoneOS game environments for historical versions of Real Racing 3. Version 8.5.0 contains a 5,807,536,488-byte Windows/Mac PC package and separate Android Adreno and Mali packages. Searching the uploader/item prefix `rr-3-armageddon-v-` reveals multiple preserved versions.

### bbvp_20251226

Internet Archive item: `https://archive.org/details/bbvp_20251226`

Title: Beat Beat Vocaloid Plus 1.8.18 and data files. This is a rhythm-game preservation item in the `apkarchive` and `phonesoftware` collections. It contains `Beat.Beat.Vocaloid.Plus.ver.1.8.18.build.60.apk` (19,964,844 bytes) and `KGS.7z` (171,921,886 bytes). The preserved data is incomplete, but some songs remain playable.

### Labyrinthofthegoblin

Internet Archive item: `https://archive.org/details/Labyrinthofthegoblin`

A discontinued Android game whose APK depended on server downloads. The uploader extracted the remaining data from an old tablet. The item contains the APK and `com.ggee.vividruntime.gg_919.zip` with the downloaded game data. It belongs to `apkarchive` and `phonesoftware`.

### wheres-my-perry-1.7.1-all-dlc-preserved-by-alleyway-jack

Internet Archive item: `https://archive.org/details/wheres-my-perry-1.7.1-all-dlc-preserved-by-alleyway-jack`

The item preserves the APK, data and OBB with all DLC. It is another example in the `apkarchive` and `phonesoftware` collections of server-dependent Android content being repackaged for preservation.

## General emulator-image repositories and candidates

### ldplayer_202506

Internet Archive item: `https://archive.org/details/ldplayer_202506`

Contains `LDPlayer.ldbk`, 6,920,343,447 bytes, MD5 `be7859509f32b1a0d1e1761d79ddf8f4`, SHA-1 `1c1bb546b403a3db2314db03cc7dddbd9400767e`. The description does not identify the installed applications, so it is a candidate requiring read-only inspection. Partial inspection confirmed that `.ldbk` starts with the 7-Zip signature.

### BackupNoxPlayer

Internet Archive item: `https://archive.org/details/BackupNoxPlayer`

Contains a 32-GiB sparse Nox VMDK stored in a 401,080,320-byte file. Read-only mounting showed a real Android filesystem, but the installed applications were root/Xposed utilities, Play Store and emulator tools rather than a game collection. This item can be discarded for SEVEN'S CODE, while demonstrating that public Nox virtual disks can be inspected without booting them.

### talkback-memu-71-2019121600013-fff-disk-2

Internet Archive item: `https://archive.org/details/talkback-memu-71-2019121600013-fff-disk-2`

Contains a MEmu 7.0.9 Android 7.1.2 OVA and its VMDK. The uploader explicitly states that no external applications are installed, so it is a clean base image rather than a game backup.

### genymotion-some-images

Internet Archive item: `https://archive.org/details/genymotion-some-images`

Contains 16 Genymotion OVA images from Android 4.1 through Android 10. These are useful base images but not installed-game snapshots.

### BlueStacksHDAppPlayerPro2.5.4.8001OfflineRootedMod

Internet Archive item: `https://archive.org/details/BlueStacksHDAppPlayerPro2.5.4.8001OfflineRootedMod`

A rooted/modded BlueStacks installer containing tools such as Titanium Backup. It is not a user snapshot, but its collection (`firmwarelibrary`, `softwarecapsules`) is another place where emulator packages and modified builds appear.

## Collections and search directories

Primary Internet Archive collections:

- `https://archive.org/details/apkarchive`
- `https://archive.org/details/phonesoftware`
- `https://archive.org/details/open_source_software`
- `https://archive.org/details/opensource_media`
- `https://archive.org/details/softwarelibrary`

Useful filename and metadata terms:

- `.npbk` — Nox exported backup; confirmed as a 7-Zip container in the inspected example.
- `.ldbk` — LDPlayer exported backup; confirmed as a 7-Zip container in the inspected example.
- `.vmdk`, `.vhdx`, `.vdi`, `.ova`, `.ovf`, `.qcow2` — emulator or VM disks.
- `Android Data Files`, `server files`, `server downloaded`, `all DLC preserved`, `APK and data files`, `Nox Backup with Server Files`.
- Game-family searches should include `rhythm game`, `music game`, `mobile game preservation`, `shutdown`, `end of service`, `offline`, `data files`, and known uploader/project prefixes.

## False positive

The Internet Archive item `nox-backups` is not a library of Nox emulator images. Its outer RAR contains password-protected archives named `backup20250612144546.rar`, `keys.rar`, `wallet.rar`, and `workspace.rar`. It should not be treated as a game-preservation source.

## Implication for SEVEN'S CODE

No broad public snapshot examined so far contains the exact SEVEN'S CODE package. However, the public examples prove that emulator backups with complete server-downloaded mobile-game data do exist and are commonly described by backup format, game version, uploader project or generic phrases rather than by package name. The next systematic search should enumerate `.npbk`, `.ldbk`, VMDK/VDI/VHDX/OVA items and scan their read-only filesystems for `jp.co.applibot.ghmabgzaxkx`, `octocacheevai`, or `files/octo`.