# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]
### Added
* Add town hubs
* Add unittests for actions
* Add parties
* Add player characters
* Read a user id in request headers
* Add marker to skip database tests
### Changed
* Make storage tests standard
* Move parsing logic away from entities
* Improve project structure to avoid circular imports

## [0.3.0] - 2022-04-29
### Added
* Add command line interface for tasks
* Add linters to dev tools
### Changed
* Change dependency manager to Poetry
* Change name of system storage


## [0.2.0] - 2022-02-18
### Added
* Add support to heroku database configuration
* Add resolver to query list of campaings from store
* Seed script for database
* Database adapter for PostgreSQL
* Store for campaigns
* Dockerize project

## [0.1.0] - 2022-02-18
### Added
* Entities for campaign manager
* Entities for town manager
* Basic GraphQL schema
