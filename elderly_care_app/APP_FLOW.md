# App Flow

This note is a viva-oriented summary of how the app flows from elderly usage to caretaker analytics and reports.

## 1. Entry And Role Flow

- App startup: `lib/main.dart`
- Auth helpers: `lib/services/auth_service.dart`
- Elderly entry UI: `lib/screens/auth/elderly_initial_login_screen.dart`
- Caretaker entry UI: `lib/screens/auth/caretaker_login_screen.dart`
- Caretaker registration: `lib/screens/auth/caretaker_registration_screen.dart`

## 2. Elderly Game Flow

- Elderly dashboard: `lib/screens/elderly/home/elderly_dashboard.dart`
- Game zone selector: `lib/screens/elderly/zone_selection_screen.dart`
- Chill Zone launcher: `lib/screens/elderly/chill_zone_screen.dart`
- Daily Engagement launcher: `lib/screens/elderly/daily_engagement_screen.dart`

### Chill Zone

- Color Tap: `lib/games/chill_zone/color_tap/color_tap_game.dart`
- Flip Card Match: `lib/games/chill_zone/flip_card_match/flip_card_game.dart`
- Shared save layer: `lib/services/game_services/session_tracker.dart`
- Shared session model: `lib/models/cognitive/game_session.dart`

### Daily Engagement

- City Atlas: `lib/games/daily_engagement/city_atlas/city_atlas_game.dart`
- Event Ordering: `lib/games/daily_engagement/event_ordering/event_ordering_game.dart`
- Daily Routine Recall: `lib/games/daily_engagement/daily_routine_recall/daily_routine_recall_game.dart`
- Monument Recall: `lib/games/daily_engagement/monument_recall/monument_recall_game.dart`

## 3. Firestore Data Flow

### Chill Zone Collections

- `colorTapGameSessions`
- `flipCardGameSessions`

Chill Zone games save through `SessionTracker.endSession(...)`.

### Daily Engagement Collections

- `game_sessions`
- `user_schedules/{userId}` for Daily Routine Recall

Daily Engagement games save directly to `game_sessions` inside each game file.

### Cached Summary

- `cognitive_summary/{userId}`

This stores high-level cached cognitive values used by dashboard/report flows.

## 4. Caretaker Analytics Flow

- Main processor: `lib/services/caretaker_data_service.dart`
- Main caretaker dashboard: `lib/screens/caretaker/dashboard/caretaker_dashboard.dart`
- Detailed cognitive screen: `lib/screens/caretaker/dashboard/cognitive_health_screen.dart`

### Important Processing Functions

- `getOverallCognitiveHealth(...)`
- `getCognitiveHealthFuture(...)`
- `_computeCognitiveHealth(...)`
- `getRecentActivityFuture(...)`
- `getOverallStatisticsFuture(...)`

### Domain Mapping Summary

- `colorTapGameSessions` -> `attention`, `processingSpeed`
- `flipCardGameSessions` -> `memory`
- `game_sessions` -> `executiveFunction`, `language`, extra `memory`

### Overall Score

- `overallScore = average(available domain scores)`

## 5. Game Analytics Screens

- Color Tap: `lib/screens/caretaker/analytics/color_tap_analytics_screen.dart`
- Flip Card: `lib/screens/caretaker/analytics/flip_card_analytics_screen.dart`
- City Atlas: `lib/screens/caretaker/analytics/city_atlas_analytics_screen.dart`
- Event Ordering: `lib/screens/caretaker/analytics/event_ordering_analytics_screen.dart`
- Daily Routine Recall: `lib/screens/caretaker/analytics/daily_routine_analytics_screen.dart`
- Monument Recall: `lib/screens/caretaker/analytics/monument_recall_analytics_screen.dart`

Each analytics screen follows the same pattern:

1. Call one `CaretakerDataService.get...Analytics(userId)` function.
2. Receive `stats` and `sessions`.
3. Show summary cards.
4. Plot trends from `sessions` using charts.

## 6. AI Cognitive Report Flow

- Report generator: `lib/services/cognitive_report_service.dart`
- Report list screen: `lib/screens/caretaker/reports/ai_cognitive_reports_screen.dart`
- Report detail screen: `lib/screens/caretaker/reports/ai_report_detail_screen.dart`

### Important Report Functions

- `generateDailyCognitiveReportIfMissing(...)`
- daily/weekly/monthly/yearly report generation helpers in `cognitive_report_service.dart`
- `_generateReportNow()` in `ai_cognitive_reports_screen.dart`

## 7. Medication And Alert Flow

- Notifications: `lib/services/notification_service.dart`
- Medication sync scheduler: `lib/services/medication_notification_service.dart`
- Elderly medication screen: `lib/screens/elderly/medication/medication_list_screen.dart`
- Caretaker alert/activity view: `lib/screens/caretaker/dashboard/buddy_activity_log_screen.dart`

## 8. One-Line End-To-End Flow

`main.dart -> auth screen -> elderly dashboard -> zone selection -> game -> Firestore session save -> caretaker_data_service -> caretaker dashboard / analytics screen -> cognitive_report_service -> AI reports screens`
