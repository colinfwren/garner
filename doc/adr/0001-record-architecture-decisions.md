# 1. Record architecture decisions

Date: 2025-08-30

## Status

Accepted

## Context

Garner will be an open source project. As such there's a potential that other developers will contribute so it's useful to have a means of documenting the decisions that are made.

## Decision

Will use `adr-tools-python` package to manage ADRs

## Consequences

When proposing a new architctural approach there will need to be a new ADR created (using `adr-new <name of record>`) and a PR raised. That PR and it's branch will then record the discussion around the proposal and it's outcome.
