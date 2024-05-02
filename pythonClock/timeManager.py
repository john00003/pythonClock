class TimeManager:
    def __init__(self, unit, ns_per_unit, ns_per_cycle, clocks):
        self.unit = unit
        self.ns_per_unit = ns_per_unit
        self.ns_per_cycle = ns_per_cycle
        self.units_per_cycle = ns_per_cycle / ns_per_unit
        self.clocks = clocks

        # TODO: delete itself if clocks is empty (no clocks use this time manager)

    def update(self, ns_time):
        utc_unit = (ns_time % self.ns_per_cycle) // self.ns_per_unit
        for clock in self.clocks:
            index = clock.time_fields.index(self.unit)
            clock.updated_time_fields[index] = utc_unit
