# Resolve workflow and operational limits

## Access and preservation
Use available documented Resolve scripting interfaces for precise supported operations. Use supported native UI tools for controls not exposed by the API. Inspect capabilities rather than invent API calls. Inspect current state again after user input or reconnection. Never use stale coordinates or track IDs. Keep one writer in control; if simultaneous input invalidates a UI action, refresh observation rather than replaying it blindly.

Before mutation, record relevant item identities, track assignments, source ranges, timing and settings in a lightweight local manifest where available. Save normally when Resolve is responsive. Do not issue saves, exports or other mutations while tracking or rendering blocks the application. Do not automatically make DRT backup exports: a prior workflow froze on that operation. Backups are useful only through a healthy, appropriate method, not repeated commands into a hung application.

Do not restart or force-quit automatically without applicable user authorization. If authorized, attempt graceful recovery first, then reopen and verify the actual saved state. Never restore an older backup over newer user work simply because it exists.

## Person in front of captions
This is a supported editorial pattern, not proof that the agent can execute every UI operation.

1. Inspect where animated text actually intersects the moving subject. Only mask those A-roll portions when that is the requested scope; do not force overlap by relocating text.
2. Use exactly aligned matching source footage: original A-roll below, captions in the middle, masked foreground above. Preserve source trim, retime, crop, transforms and grade. B-roll must not be covered by an unrelated foreground person.
3. On the foreground copy, use Color-page Magic Mask with Better quality when requested. Add positive selections on the face and torso as appropriate; review the overlay and exclude background spill. Existing user-created seeds and tracking should be preserved.
4. Track the required range forward and backward, wait for completion, and check motion, hair/face edges and shot boundaries. A valid mask on one frame is not tracking evidence.
5. Add/connect the node's key output to an Alpha Output on the foreground copy using verified supported controls. Confirm actual transparency. Do not apply this routing to the natural base image accidentally.
6. Inspect the composite at overlap frames and in playback. Check text readability, unwanted duplicate footage, halos, and foreground remaining over B-roll. Save once responsive.

Historical lesson: mask tracking succeeded in a prior session but alpha routing failed through the control interface. Treat this as a capability that needs live validation, not a completed integration.

## Timeline exchange
OpenTimelineIO or XML can represent structural edits but do not guarantee preservation of Fusion titles, masks, retiming or grades. Test a short isolated interchange before relying on it, inspect source mappings, and preserve the user's current timeline. Do not silently replace Resolve-native work with a flattened render.
