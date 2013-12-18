jmap
====

Here's a gentle introduction:

http://prefetch.net/blog/index.php/2007/10/27/summarizing-java-heap-utilization-with-jmap/

Getting errors like this?

    kirk@animal ~ $ jmap -heap `pgrep java`
    Attaching to process ID 6377, please wait...
    Error attaching to process: sun.jvm.hotspot.debugger.DebuggerException: Can't attach to the process

Then you need to do this (from this bug report):

    echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
