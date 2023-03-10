# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased](https://github.com/natanfeitosa/kohi/compare/v0.4.0...HEAD)

### Added

### Changed

### Fixed

### Removed

## [v0.4.0](https://github.com/natanfeitosa/kohi/compare/v0.3.0...v0.4.0) - 2023-03-07

### Added

- `DictSchema` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#9](https://github.com/natanfeitosa/kohi/issues/9))
- `BaseSchema.parse(data)` by [@natanfeitosa](https://github.com/natanfeitosa/)
- `BaseSchema.add_mutation(mutation)` by [@natanfeitosa](https://github.com/natanfeitosa/)
- `BaseSchema.default(default_value)` by [@natanfeitosa](https://github.com/natanfeitosa/)
- `BaseSchema.optional()` by [@natanfeitosa](https://github.com/natanfeitosa/)
- `BaseSchema.required(error_message)` by [@natanfeitosa](https://github.com/natanfeitosa/)

## [v0.3.0](https://github.com/natanfeitosa/kohi/compare/v0.2.0...v0.3.0) - 2023-01-26

### Added

- `BaseSchema.label(text)` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#4](https://github.com/natanfeitosa/kohi/issues/4))
- `EnumSchema` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#3](https://github.com/natanfeitosa/kohi/issues/3))
- `EnumSchema.one_of(opts)` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#3](https://github.com/natanfeitosa/kohi/issues/3))
- `EnumSchema.not_one_of(opts)` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#3](https://github.com/natanfeitosa/kohi/issues/3))

### Changed

- All validation methods, including the constructor, now accept a custom error message ([#5](https://github.com/natanfeitosa/kohi/issues/5))

## [v0.2.0](https://github.com/natanfeitosa/kohi/compare/v0.1.0...v0.2.0) - 2023-01-19

### Added

- `Number.nonpositive()` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#1](https://github.com/natanfeitosa/kohi/issues/1))
- `Number.nonnegative()` by [@natanfeitosa](https://github.com/natanfeitosa/) ([#1](https://github.com/natanfeitosa/kohi/issues/1))

## [v0.1.0](https://github.com/natanfeitosa/kohi/releases/tag/v0.1.0) - 2023-01-13

initial release
