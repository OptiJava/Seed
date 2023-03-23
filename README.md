# Seed
> Get world seed without op permission.

## Preview

![image](https://user-images.githubusercontent.com/106148777/226171691-12bcd497-35a6-4680-a113-b5754f0d435b.png)

## Configure

`config/seed/config.json`
- `command`: Command to get seed in console
- `parser`: Parser for the command result

Default config file:
```
{
    'command': 'seed',
    'parser': 'Seed: [{}]'
}
```

The default configuration already supports most server software (without plugin/mods).

## Thanks to

This plugin was inspired by [`MCDReforged/Seed`](https://github.com/MCDReforged/Seed)

Thanks to @[alex3236](https://github.com/alex3236) for refactoring the code（（
